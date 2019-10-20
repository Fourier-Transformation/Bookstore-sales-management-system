import React from 'react';
import styled from 'styled-components';
import { PUBLIC_URL } from '../constants';
import { Link } from 'react-router-dom';

export default class BookPreview extends React.Component {
    render() {
        const { name, cover } = this.props;

        return (
            <StyledBookPreview>
                <Link to='/bookdetail'><img src={ `${ PUBLIC_URL }/${ cover }` }></img></Link>
                <div className='book-name'><Link to='/bookdetail'>{ name }</Link></div>
            </StyledBookPreview>
        );
    }
}

const StyledBookPreview = styled.div`
    display: inline-block;
    margin: 10px 30px;
    position: relative;

    img {
        width:100px;
        margin-bottom: 20px;
    }

    .book-name {
        position: absolute;
        bottom: 0;
        width: 100px;
    }
    a{
        text-decoration:none;
    }
`;