import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import { Icon, Table } from 'semantic-ui-react'
import './Patients.css'

class Patients extends Component {
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
        <Table.Cell>
          <Link to={`/events/${patient.id}`}>
            Events
            <Icon name="arrow circle right alternate outline"/>
          </Link>
        </Table.Cell>
      </Table.Row>
    ))
  }

  render() {
    return (
      <div>
        <h1>Patients</h1>
        <Table celled className="patient-table">
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell>Name</Table.HeaderCell>
              <Table.HeaderCell>Tidepool Username</Table.HeaderCell>
              <Table.HeaderCell>Tidepool ID</Table.HeaderCell>
              <Table.HeaderCell></Table.HeaderCell>
            </Table.Row>
          </Table.Header>

          <Table.Body>
            {this.renderPatientList()}
          </Table.Body>

        </Table>
      </div>
    )
  }
}

export default Patients
