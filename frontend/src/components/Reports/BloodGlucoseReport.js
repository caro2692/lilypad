import React, { Component } from 'react'
import queryString from 'query-string'
import axios from 'axios'
import { Statistic } from 'semantic-ui-react'
import moment from 'moment'

class BloodGlucoseReport extends Component {
  constructor(props) {
    super(props)
    this.state = {
      patient : '',
      startDate: '',
      endDate: '',
      report: {},
    }
  }

  componentDidMount() {
    const params = queryString.parse(this.props.location.search)
    this.setState(params, () => {
      this.getReport()
    })
  }

  formatDates() {
    let { startDate, endDate } = this.state
    startDate = moment(startDate).format('YYYY-MM-DDTHH:mm:ss.SSS') + 'Z'
    endDate = moment(endDate).format('YYYY-MM-DDTHH:mm:ss.SSS') + 'Z'
    return { startDate, endDate }
  }

  getReport = () => {
    const { startDate, endDate } = this.formatDates()
    const params = { patient: this.state.patient, startDate, endDate }
    axios.get('/api/blood_glucose_report/', { params })
      .then(resp => {
        this.setState({ report: resp.data })
      })
      .catch(err => console.log(err))
  }

  render() {
    return (
      <Statistic.Group widths='three'>
        <Statistic color='blue'>
          <Statistic.Value>
            {Number(this.state.report.average_per_day).toFixed(1)}
          </Statistic.Value>
          <Statistic.Label>Average # BG checks/day</Statistic.Label>
        </Statistic>
        <Statistic color='red'>
          <Statistic.Value>
            {Number(this.state.report.lowest_per_day).toFixed(1)}
          </Statistic.Value>
          <Statistic.Label>Lowest # BG checks/day</Statistic.Label>
        </Statistic>
        <Statistic color='green'>
          <Statistic.Value>
            {Number(this.state.report.highest_per_day).toFixed(1)}
          </Statistic.Value>
          <Statistic.Label>Highest # BG checks/day</Statistic.Label>
        </Statistic>
      </Statistic.Group>
    )
  }
}

export default BloodGlucoseReport
