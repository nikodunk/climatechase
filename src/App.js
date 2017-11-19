import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import $ from 'jquery'; 

class App extends Component {

  onError(error){
    console.log(error)
  }

  constructor(props) {
    super(props);

    this.state = {
    }

  }

  componentDidMount() {
      this.getData()
  }


  getData(){
    clearTimeout()
    var url = "http://127.0.0.1:5000/"
    $.get(url).then(result => {
        this.setState(JSON.parse(result))
      }) 
    setTimeout( this.getData.bind(this), 1000)
  }


  onClick(e){
    console.log(e.target.id)
    // console.log(this.state)

    fetch('http://localhost:5000/' + e.target.id + '/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(this.state),
      success: console.log('success')
    })
    
    
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" /><h1 className="App-title">ClimateChase</h1>
        </header>
        <h1 className="subtitle" > {this.state.Curr_Year}</h1>
        <h1 className="subtitle" > GDP: ${this.state.GDP}</h1>
        <h1 className="subtitle" >Finances: ${this.state.Money}</h1>
        <hr />
        <h2>invest in</h2>
        <button onClick={this.onClick.bind(this)} id="wind">wind</button>
        <button onClick={this.onClick.bind(this)} id="solar">solar</button>
        <button onClick={this.onClick.bind(this)} id="nuclear">nuclear</button>
        <button onClick={this.onClick.bind(this)} id="fossil">fossil</button>
      </div>
    );
  }

  
}

export default App;