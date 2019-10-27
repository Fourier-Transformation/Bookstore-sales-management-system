import React from 'react';
import styled from 'styled-components';
import SearchBar from '../components/SearchBar';
import CartButton from '../components/CartButton';
import { PUBLIC_URL } from '../constants/index';

export default class Header extends React.Component {
    render() {
        return (
            <StyledHeader>
                <img src={ `${ PUBLIC_URL }/images/logo.png` } className='img'></img>
                <SearchBar />
                <CartButton />
            </StyledHeader>
        );
    }
}

const StyledHeader = styled.div`
    margin: 0 250px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    .img{
        width:230px;
    }
`;