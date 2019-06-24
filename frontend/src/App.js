import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import './App.css';
import logo from './logo.png'
import Patients from './components/Patients/Patients'
import Events from './components/Events/Events'
import BloodGlucoseReport from './components/Reports/BloodGlucoseReport'
import { Container, Menu } from 'semantic-ui-react'

class App extends Component {

  render() {
    return (
      <Router>
        <div className="App">
          <div>
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
          </div>
          <Container className="main">
            <Route exact path="/" component={Patients} />
            <Route path="/events/:id" component={Events} />
            <Route path="/report/" component={BloodGlucoseReport} />
          </Container>
        </div>
      </Router>
    )
  }
}

export default App
