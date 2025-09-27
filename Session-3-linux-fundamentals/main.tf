provider "aws" {
  region = var.region
}

data "aws_vpc" "default" {
  default = true
}
# All subnets in that VPC
data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"] # Canonical
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_security_group" "elk" {
  name        = "elk-sg"
  description = "Allow SSH, Kibana, ES, Logstash"
  vpc_id      = data.aws_vpc.default.id

  dynamic "ingress" {
    for_each = var.allowed_cidrs
    content {
      description = "SSH"
      from_port   = 22
      to_port     = 22
      protocol    = "tcp"
      cidr_blocks = [ingress.value]
    }
  }

  dynamic "ingress" {
    for_each = var.allowed_cidrs
    content {
      description = "Kibana"
      from_port   = 5601
      to_port     = 5601
      protocol    = "tcp"
      cidr_blocks = [ingress.value]
    }
  }

  dynamic "ingress" {
    for_each = var.allowed_cidrs
    content {
      description = "Elasticsearch"
      from_port   = 9200
      to_port     = 9200
      protocol    = "tcp"
      cidr_blocks = [ingress.value]
    }
  }

  dynamic "ingress" {
    for_each = var.allowed_cidrs
    content {
      description = "Logstash TCP"
      from_port   = 5000
      to_port     = 5000
      protocol    = "tcp"
      cidr_blocks = [ingress.value]
    }
  }

  dynamic "ingress" {
    for_each = var.allowed_cidrs
    content {
      description = "Logstash Beats"
      from_port   = 5044
      to_port     = 5044
      protocol    = "tcp"
      cidr_blocks = [ingress.value]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "elk-sg"
  }
}

resource "aws_instance" "elk" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = var.instance_type
  subnet_id              = data.aws_subnets.default.ids[0]
  vpc_security_group_ids = [aws_security_group.elk.id]
  key_name               = var.key_name

  root_block_device {
    volume_size = var.volume_size
    volume_type = "gp3"
  }

  user_data = <<-EOF
    #!/bin/bash
    set -euxo pipefail
    apt-get update -y
    apt-get install -y docker.io docker-compose-plugin jq
    systemctl enable --now docker
    sysctl -w vm.max_map_count=262144
    echo "vm.max_map_count=262144" > /etc/sysctl.d/60-elastic.conf

    mkdir -p /opt/elk/logstash/pipeline

    cat > /opt/elk/docker-compose.yml <<'YAML'
    version: '3.8'
    services:
      elasticsearch:
        image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
        container_name: elasticsearch
        environment:
          - discovery.type=single-node
          - xpack.security.enabled=false
          - ES_JAVA_OPTS=-Xms1g -Xmx1g
        ulimits:
          memlock:
            soft: -1
            hard: -1
        volumes:
          - esdata:/usr/share/elasticsearch/data
        ports:
          - "9200:9200"
        networks: [elk]

      kibana:
        image: docker.elastic.co/kibana/kibana:8.11.0
        container_name: kibana
        environment:
          - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
        depends_on: [elasticsearch]
        ports:
          - "5601:5601"
        networks: [elk]

      logstash:
        image: docker.elastic.co/logstash/logstash:8.11.0
        container_name: logstash
        volumes:
          - ./logstash/pipeline:/usr/share/logstash/pipeline:ro
        depends_on: [elasticsearch]
        ports:
          - "5000:5000"
          - "5044:5044"
          - "9600:9600"
        networks: [elk]

    volumes:
      esdata:
    networks:
      elk:
    YAML

    cat > /opt/elk/logstash/pipeline/logstash.conf <<'CONF'
    input {
      tcp {
        port => 5000
        codec => json_lines
      }
      beats {
        port => 5044
      }
    }
    filter { }
    output {
      stdout { codec => rubydebug }
      elasticsearch {
        hosts => ["http://elasticsearch:9200"]
        index => "logs-%%{+YYYY.MM.dd}"
      }
    }
    CONF

    cd /opt/elk
    docker compose up -d
  EOF

  tags = {
    Name = "elk-ec2"
  }
}
