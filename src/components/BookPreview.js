import React from 'react';
import styled from 'styled-components';
import { PUBLIC_URL } from '../constants';

export default class BookPreview extends React.Component {
    render() {
        const { name, cover } = this.props;

        return (
            <StyledBookPreview>
                <img src={ `${ PUBLIC_URL }/${ cover }` }></img>
                <div>{ name }</div>
            </StyledBookPreview>
        );
    }
}

const StyledBookPreview = styled.div`
    display: inline-block;
`;