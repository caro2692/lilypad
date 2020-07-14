import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import { Form, Header, Icon, Input, Table } from 'semantic-ui-react'
import './Patients.css'

class Patients extends Component {
  constructor(props) {
    super(props)
    this.state = {
      patients: [],
      tidepoolID: '',
      patientExists: false,
    }

    this.handleIDChange = this.handleIDChange.bind(this)
  }

  componentDidMount() {
    this.getPatients()
  }

  handleIDChange(event) {
    this.setState({tidepoolID: event.target.value})
  }

  getPatients = () => {
    axios.get('/api/patient/')
      .then(resp => this.setState({ patients: resp.data }))
      .catch(err => console.log(err))
  }

  addPatient = () => {
    axios.post(`/api/patient/${this.state.tidepoolID}/add_from_tidepool/`)
      .then(resp => {
        this.getPatients()
        this.setState({ patientExists: resp.status === 201 })
      })
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
        <Form onSubmit={this.addPatient}>
          <Form.Group>
            <Form.Field inline>
              <label>Add patient by Tidepool ID:</label>
              <Input placeholder="Tidepool ID"
                  value={this.state.tidepoolID}
                  onChange={this.handleIDChange} />
            </Form.Field>
            <Form.Button primary type='submit'>
              Add Patient
            </Form.Button>
            <Header size='small' color='red' floated='right'>
              {this.state.patientExists ? 'Patient already exists' : null}
            </Header>
          </Form.Group>
        </Form>
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
