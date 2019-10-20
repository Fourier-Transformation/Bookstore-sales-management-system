import React from 'react';
import styled from 'styled-components';
import BookPreview from '../components/BookPreview';
import { BOOKS_COUNT_PER_PAGE, PUBLIC_URL } from '../constants';

export default class BookList extends React.Component {
    state = {
        bookList: []
    }

    async componentDidMount() {
        const res = await fetch(`${ PUBLIC_URL }/mock/booklist.json`);
        const data = await res.json();

        this.setState({
            bookList: data
        });
    }

    renderList() {
        const { bookList } = this.state;

        return bookList.map(({ name, cover }) => {
            return <BookPreview name={ name } cover={ cover } />
        })
    }

    render() {
        const { bookList } = this.state;

        return (
            <React.Fragment>
                { bookList ? this.renderList() : null }
            </React.Fragment>
        );
    }
}