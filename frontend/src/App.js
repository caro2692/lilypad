import React, { Component } from 'react';
import './App.css';
import axios from 'axios'
import logo from './logo.png'
import { Container, Menu, Table } from 'semantic-ui-react'

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      patients: []
    }
  }

  componentDidMount() {
    this.getPatients()
  }

  getPatients = () => {
    axios.get('/api/patient/')
      .then(resp => this.setState({ patients: resp.data }))
      .catch(err => console.log(err))
  }

  renderPatientList = () => {
    const patients = this.state.patients.filter(p => p.active)
    return patients.map(patient => (
      <Table.Row key={patient.id}>
        <Table.Cell>{ patient.name }</Table.Cell>
        <Table.Cell>{ patient.tidepool_username }</Table.Cell>
        <Table.Cell>{ patient.tidepool_userid }</Table.Cell>
      </Table.Row>
    ))
  }

  render() {
    return (
      <div className="App">
        <header>
          <Menu fixed="top" size="large" inverted borderless className="App-header">
            <Container>
              <Menu.Item>
                <img src={logo} alt="logo" />
              </Menu.Item>
              <Menu.Item>Lilypad</Menu.Item>
            </Container>
          </Menu>
        </header>
        <Container className="main">
          <h1>Patients</h1>

          <Table celled>
            <Table.Header>
              <Table.Row>
                <Table.HeaderCell>Name</Table.HeaderCell>
                <Table.HeaderCell>Tidepool Username</Table.HeaderCell>
                <Table.HeaderCell>Tidepool ID</Table.HeaderCell>
              </Table.Row>
            </Table.Header>

            <Table.Body>
              {this.renderPatientList()}
            </Table.Body>

          </Table>
        </Container>
      </div>
    )
  }
}

export default App;
