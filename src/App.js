import React from 'react';
import './App.css';

import TopBar from './components/TopBar';
import Header from './containers/Header';
import Categories from './components/Categories'
import BookList from './containers/BookList';

class App extends React.Component {
  render() {
    return  (
      <div className="App">
        <TopBar />
        <Header />
        <Categories />
        <BookList />
      </div>
    );
  }
}

export default App;
