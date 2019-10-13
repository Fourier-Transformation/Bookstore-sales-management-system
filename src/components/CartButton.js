import React from 'react';
import styled from 'styled-components';

export default class CartButton extends React.Component {
    render() {
        return (
            <StyledCartButton>
                购物车
            </StyledCartButton>
        );
    }
}

const StyledCartButton = styled.div`
    display: inline-block;
    width: 72px;
    height: 37px;
    margin-top: 18px;
    background: red;
    line-height: 37px;
    color: white;
    cursor: pointer;
`;