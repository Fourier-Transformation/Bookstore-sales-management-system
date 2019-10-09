import React from 'react';
import './App.css';

import TopBar from './components/TopBar';
import Header from './containers/Header';
import Categories from './components/Categories'

class App extends React.Component {
  render() {
    return  (
      <div className="App">
        <TopBar />
        <Header />
        <Categories />
      </div>
    );
  }
}

export default App;
