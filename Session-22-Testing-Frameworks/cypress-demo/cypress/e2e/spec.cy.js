describe('My First Test', () => {
  it('clicks the link', () => {
    cy.visit('https://example.cypress.io')
    cy.contains('type').click()
    cy.url().should('include','/commands/actions')
    cy.get('.action-email').type('sonam@gmail.com')
    cy.get('.action-email').should('have.value', 'sonam@gmail.com')
  })
})