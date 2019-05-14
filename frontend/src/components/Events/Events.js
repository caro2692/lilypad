import React, { Component } from 'react'

class Events extends Component {
  constructor(props) {
    super(props)
    this.state = {
      patientId : props.match.params.id
    }
  }
  render() {
    return (
      <div>
        <h1>Patient: {this.state.patientId}</h1>
      </div>
    )
  }
}

export default Events
