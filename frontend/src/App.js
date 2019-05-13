import React from 'react';
import './App.css';
import logo from './logo.png'
import { Container, Menu, Table } from 'semantic-ui-react'

function App() {
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
        <Table celled>

          <Table.Header>
            <Table.Row>
              <Table.HeaderCell>Header</Table.HeaderCell>
              <Table.HeaderCell>Header</Table.HeaderCell>
              <Table.HeaderCell>Header</Table.HeaderCell>
            </Table.Row>
          </Table.Header>

          <Table.Body>
            <Table.Row>
              <Table.Cell>blah</Table.Cell>
              <Table.Cell>blah</Table.Cell>
              <Table.Cell>blah</Table.Cell>
            </Table.Row>
          </Table.Body>

        </Table>
      </Container>
    </div>
  );
}

export default App;
