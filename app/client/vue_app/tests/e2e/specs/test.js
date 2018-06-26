// https://docs.cypress.io/api/introduction/api.html

describe('My First Test', () => {
  it('Visits the app root url', () => {
    cy.visit('/')
    cy.contains('h1', 'BigRep HMI Demo')
  })
  it('It has a button connect to printer', () => {
    cy.visit('/')
    cy.contains('button', 'Connect to printer')
  })
})
