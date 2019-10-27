import React from 'react';
import TopBar from '../components/TopBar';
import Header from '../containers/Header';
import Categories from '../components/Categories';

export default class CommonHeader extends React.Component {
    render() {
        return (
            <React.Fragment>
                <TopBar />
                <Header />
                <Categories />
            </React.Fragment>
        );
    }
}