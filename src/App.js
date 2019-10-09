import React from 'react';
import './App.css';

import TopBar from './components/TopBar';
import Header from './containers/Header';

class App extends React.Component {
  render() {
    return  (
      <div className="App">
        <TopBar />
        <Header />
      </div>
    );
  }
}

export default App;
