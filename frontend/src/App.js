import React, { Component } from 'react';
import './App.css';
import logo from './logo.png'
import Patients from './components/Patients/Patients'
import { Container, Menu } from 'semantic-ui-react'

class App extends Component {

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
          <Patients />
        </Container>
      </div>
    )
  }
}

export default App;
