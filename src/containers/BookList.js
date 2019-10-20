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
        }).concat([<i></i>,<i></i>,<i></i>,<i></i>,<i></i>])
    }

    render() {
        const { bookList } = this.state;

        return (
            <StyledBookList>
                { bookList ? this.renderList() : null }
            </StyledBookList>
        );
    }
}

const StyledBookList = styled.div`
    max-width: 1000px;
    margin: 20px auto;
    display: flex;
    flex-wrap: wrap;
    align-content: center;
    justify-content: space-around;

    i {
        width: 100px;
        margin: 0 30px;
    }
`;