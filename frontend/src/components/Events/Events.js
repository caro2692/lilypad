import React, { Component } from 'react'
import axios from 'axios'
import { Table } from 'semantic-ui-react'
import moment from 'moment'

class Events extends Component {
  constructor(props) {
    super(props)
    this.state = {
      patientId : props.match.params.id,
      events: []
    }
  }

  componentDidMount() {
    this.getEventsForPatient()
  }

  getEventsForPatient = () => {
    axios.get(`/api/patient/${this.state.patientId}/events`)
      .then(resp => this.setState({ events: resp.data }))
      .catch(err => console.log(err))
  }

  renderEventList = () => {
    const events = this.state.events.filter(e => e.active)
    return events.map(event => (
      <Table.Row key={event.id}>
        <Table.Cell>{ event.id }</Table.Cell>
        <Table.Cell>{ event.device_id }</Table.Cell>
        <Table.Cell>{ event.tidepool_id }</Table.Cell>
        <Table.Cell>{ event.tidepool_guid }</Table.Cell>
        <Table.Cell>{ moment(event.time).format('M/D/YYYY, LT') }</Table.Cell>
        <Table.Cell>{ moment(event.created_at).format('M/D/YYYY, LT') }</Table.Cell>
        <Table.Cell>{ moment(event.updated_at).format('M/D/YYYY, LT') }</Table.Cell>
        <Table.Cell>{ event.value } { event.units }</Table.Cell>
      </Table.Row>
    ))
  }

  render() {
    return (
      <div>
        <h1>Events</h1>
        <Table celled className="patient-table">
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell>ID</Table.HeaderCell>
              <Table.HeaderCell>Device ID</Table.HeaderCell>
              <Table.HeaderCell>Tidepool ID</Table.HeaderCell>
              <Table.HeaderCell>Tidepool GUID</Table.HeaderCell>
              <Table.HeaderCell>Time</Table.HeaderCell>
              <Table.HeaderCell>Created At</Table.HeaderCell>
              <Table.HeaderCell>Updated At</Table.HeaderCell>
              <Table.HeaderCell>Value</Table.HeaderCell>
            </Table.Row>
          </Table.Header>

          <Table.Body>
            {this.renderEventList()}
          </Table.Body>

        </Table>
      </div>
    )
  }
}

export default Events
