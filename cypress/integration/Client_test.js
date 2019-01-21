describe('Sanity Checks', function() {
  it('Visits the sanity check site', function() {
    cy.visit('http://localhost:8080/ping')
    cy.url().should('include', '/ping')
  })
  it('Checks if pong is returned', function() {
    cy.visit('http://localhost:8080/ping')
    cy.get('.btn').contains('pong!')
  })
})
describe('Frontend Testing', function() {
  it('Visits the main site', function() {
    cy.visit('http://localhost:8080/')
  })
  it('Opens the Add User Popup', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#user-modal___BV_modal_body_')
  })
  it('Resets the Add User Popup', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#form-username-input').type('Michael')
	cy.get('#form-email-input').type('mwintersperger@student.tgm.ac.at')
	cy.get('#form-photo-input').type('test.jepg')
	cy.get('#user-modal___BV_modal_body_ > .w-100 > .btn-danger').click()
  })
  it('Closes the Add User Popup', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#form-username-input').type('Michael')
	cy.get('#form-email-input').type('mwintersperger@student.tgm.ac.at')
	cy.get('#form-photo-input').type('test.jepg')
	cy.get('#user-modal___BV_modal_header_ > .close').click()
  })
  it('Enters a User with invalid Username', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#form-username-input').type('Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore')
	cy.get('#form-email-input').type('mwintersperger@student.tgm.ac.at')
	cy.get('#form-photo-input').type('test.jepg')
	cy.get('#user-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
	// As this fails i manualy do a POST request
	cy.request('POST', 'http://localhost:5000/users', { username: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lore', email: 'mwintersperger@student.tgm.ac.at', photo: 'test.jpeg'})
  .then((response) => {
    // response.body is automatically serialized into JSON
    expect(response.body).to.have.property('status', 'failure')
    expect(response.body).to.have.property('message', 'Username too long!')
  })
  })
  it('Enters a User with invalid email', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#form-username-input').type('Michael')
	cy.get('#form-email-input').type('mwinterspergerstudent.tgm.ac.at')
	cy.get('#form-photo-input').type('test.jepg')
	cy.get('#user-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
	// As this fails i manualy do a POST request
	cy.request('POST', 'http://localhost:5000/users', { username: 'Michael', email: 'mwinterspergerstudent.tgm.ac.at', photo: 'test.jpeg'})
  .then((response) => {
    // response.body is automatically serialized into JSON
    expect(response.body).to.have.property('status', 'failure')
    expect(response.body).to.have.property('message', 'Email is not valid!')
  })
  })
  it('Enters a User with invalid photo', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#form-username-input').type('Michael')
	cy.get('#form-email-input').type('mwintersperger@student.tgm.ac.at')
	cy.get('#form-photo-input').type('bla.jepg')
	cy.get('#user-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
	// As this fails i manualy do a POST request
	cy.request('POST', 'http://localhost:5000/users', { username: 'Michael', email: 'mwintersperger@student.tgm.ac.at', photo: 'bla.jpeg'})
  .then((response) => {
    // response.body is automatically serialized into JSON
    expect(response.body).to.have.property('status', 'failure')
    expect(response.body).to.have.property('message', 'Image not valid!')
  })
  })
  it('Enters a Valid User', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#form-username-input').type('Michael')
	cy.get('#form-email-input').type('mwintersperger@student.tgm.ac.at')
	cy.get('#form-photo-input').type('test.jepg')
	cy.get('#user-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
	// As this fails i manualy do a POST request
	cy.request('POST', 'http://localhost:5000/users', { username: 'Michael', email: 'mwintersperger@student.tgm.ac.at', photo: 'test.jpeg'})
  .then((response) => {
    // response.body is automatically serialized into JSON
    expect(response.body).to.have.property('status', 'success')
    expect(response.body).to.have.property('message', 'User added!')
  })
  cy.wait(500)
  cy.get('tbody > tr > :nth-child(1)').contains('Michael')
  cy.get('tbody > tr > :nth-child(2)').contains('mwintersperger@student.tgm.ac.at')
  cy.get('tbody > tr > :nth-child(3)').contains('test.jpeg')
  })
  it('Adds a User with an existing Email', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#form-username-input').type('Michael')
	cy.get('#form-email-input').type('mwintersperger@student.tgm.ac.at')
	cy.get('#form-photo-input').type('test.jepg')
	cy.get('#user-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
	// As this fails i manualy do a POST request
	cy.request('POST', 'http://localhost:5000/users', { username: 'Michael', email: 'mwintersperger@student.tgm.ac.at', photo: 'test.jpeg'})
  .then((response) => {
    // response.body is automatically serialized into JSON
    expect(response.body).to.have.property('status', 'failure')
    expect(response.body).to.have.property('message', 'Email already exists!')
  })
  })
  it('Updates the username', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.btn-warning').click()
	cy.get('#form-username-edit-input').clear()
	cy.get('#form-username-edit-input').type('Michael2')
	cy.get('#user-update-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
    cy.get('tbody > tr > :nth-child(1)').contains('Michael2')
	cy.get('.alert').contains('User updated!')
  })
    it('Updates the email', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.btn-warning').click()
	cy.get('#form-email-edit-input').clear()
	cy.get('#form-email-edit-input').type('mwintersperger2@student.tgm.ac.at')
	cy.get('#user-update-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
    cy.get('tbody > tr > :nth-child(2)').contains('mwintersperger2@student.tgm.ac.at')
	cy.get('.alert').contains('User updated!')
  })
  it('Updates the photo', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.btn-warning').click()
	cy.get('#form-photo-edit-input').clear()
	cy.get('#form-photo-edit-input').type('test2.jpeg')
	cy.get('#user-update-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
    cy.get('tbody > tr > :nth-child(3)').contains('test2.jpeg')
	cy.get('.alert').contains('User updated!')
  })
  it('Updates the email with an already existing email', function() {
    cy.visit('http://localhost:8080/')
	cy.get('.col-sm-10 > .btn').click()
	cy.get('#form-username-input').type('Michael')
	cy.get('#form-email-input').type('mwintersperger@student.tgm.ac.at')
	cy.get('#form-photo-input').type('test.jepg')
	cy.get('#user-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
	// As this fails i manualy do a POST request
	cy.request('POST', 'http://localhost:5000/users', { username: 'Michael', email: 'mwintersperger@student.tgm.ac.at', photo: 'test.jpeg'})
  .then((response) => {
    // response.body is automatically serialized into JSON
    expect(response.body).to.have.property('status', 'success')
    expect(response.body).to.have.property('message', 'User added!')
  })
    cy.get('.btn-warning').last().click()
    cy.get('#form-email-edit-input').clear()
    cy.get('#form-email-edit-input').type('mwintersperger2@student.tgm.ac.at')
    cy.get('#user-update-modal___BV_modal_body_ > .w-100 > .btn-primary').click()
	cy.wait(500)
    cy.get('.alert').contains('Email already exists!')
  })
  it('Deletes the User', function() {
	cy.wait(500)
    cy.visit('http://localhost:8080/')
	cy.get(':nth-child(1) > :nth-child(4) > .btn-danger').click()
	cy.get(':nth-child(2) > :nth-child(4) > .btn-danger').click()
  })
})