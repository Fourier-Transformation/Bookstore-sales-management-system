import React from 'react';
import './App.css';

import TopBar from './components/TopBar';
import Header from './containers/Header';
import BookList from './containers/BookList';

class App extends React.Component {
  render() {
    return  (
      <div className="App">
        <TopBar />
        <Header />
        <BookList />
      </div>
    );
  }
}

export default App;
