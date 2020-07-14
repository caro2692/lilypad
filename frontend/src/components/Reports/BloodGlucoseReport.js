import React, { Component } from 'react'
import queryString from 'query-string'
import axios from 'axios'
import { Header, Segment, Statistic } from 'semantic-ui-react'
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

  statColor(val, low = 2, high = 4) {
    return {
      'red': val <= low,
      'orange': low < val < high,
      'green': val >= high,
    }
  }

  render() {
    return (
      <div>
        <Header as='h1' dividing>{this.state.report.patient_name}
          <Header.Subheader>
            {moment(this.state.startDate).format('M/D/YYYY')} to {moment(this.state.endDate).format('M/D/YYYY')}
          </Header.Subheader>
        </Header>
        <Segment.Group>
          <Segment secondary>
            <h3>Blood Glucose Checks</h3>
          </Segment>
          <Segment>
            <Statistic.Group widths='three'>
              <Statistic color={this.statColor(this.state.report.average_per_day)}>
                <Statistic.Value>
                  {Number(this.state.report.average_per_day).toFixed(1)}
                </Statistic.Value>
                <Statistic.Label>Average # BG checks/day</Statistic.Label>
              </Statistic>
              <Statistic color={this.statColor(this.state.report.lowest_per_day)}>
                <Statistic.Value>
                  {Number(this.state.report.lowest_per_day).toFixed(1)}
                </Statistic.Value>
                <Statistic.Label>Lowest # BG checks/day</Statistic.Label>
              </Statistic>
              <Statistic color={this.statColor(this.state.report.highest_per_day)}>
                <Statistic.Value>
                  {Number(this.state.report.highest_per_day).toFixed(1)}
                </Statistic.Value>
                <Statistic.Label>Highest # BG checks/day</Statistic.Label>
              </Statistic>
            </Statistic.Group>
          </Segment>
        </Segment.Group>
      </div>
    )
  }
}

export default BloodGlucoseReport
