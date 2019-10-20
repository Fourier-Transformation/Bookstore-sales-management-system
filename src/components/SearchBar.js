import React from 'react';
import styled from 'styled-components';

export default class SearchBar extends React.Component {
    render() {
        return (
            <StyledSearchBarContainer>
                <StyledSearchBar></StyledSearchBar>
                <StyledSearchButton>搜索</StyledSearchButton>
            </StyledSearchBarContainer>
        );
    }
}

const baseStyles = `
    height: 18px;
    margin-top: 20px;
    padding: 9px 0 9px 10px;
`;

const StyledSearchBarContainer = styled.div`
    position: relative;
`;

const StyledSearchBar = styled.input`
    ${ baseStyles }
    width: 398px;
    outline: none;
    border: 2px solid red;
`

const StyledSearchButton = styled.div`
    ${ baseStyles }
    color: white;
    background: red;
    display: inline-block;
    position: absolute;
    right: 0px;
    top: 2px;
    width: 50px;
    padding-right: 10px;
    cursor: pointer;
`;