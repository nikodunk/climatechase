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
    var url = "http://127.0.0.1:5000/"
        $.get(url).then(result => {
            this.setState(JSON.parse(result))
          })
        console.log(this.state)   
  }


  onClick(e){
    console.log(e.target.id)
    console.log(this.state)

    $.ajax({
      type: "POST",
      url: 'http://localhost:5000/' + e.target.id + '/',
      data: this.state,
      success: result => console.log(result),
    });
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