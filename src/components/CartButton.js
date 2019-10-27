import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

export default class CartButton extends React.Component {
    render() {
        return (
            <Link to='/payment'>
                <StyledCartButton>购物车</StyledCartButton>
            </Link>
        );
    }
}

const StyledCartButton = styled.div`
    display: flex;
    width: 72px;
    height: 37px;
    margin-top: 18px;
    background: red;
    line-height: 37px;
    color: white;
    flex-wrap: wrap;
    align-content: flex-end;
    justify-content: space-around;
    cursor:pointer;
`;