import React from 'react';
import styled from 'styled-components';
import { PUBLIC_URL } from '../constants';
import { Link } from 'react-router-dom';
import { Card } from 'antd';

const { Meta } = Card;

export default class BookPreview extends React.Component {
    trimDescription(str) {
        return str.length > 50 ? `${ str.slice(0, 50) }...` : str;
    }

    render() {
        const { name, cover, description } = this.props;

        return (
            <StyledBookPreview>
                <Card
                    hoverable
                    style={{ width: 240 }}
                    cover={<img alt={ name } src={ cover } />}
                    className='preview-card'
                >
                    <Meta title={ name } description={ this.trimDescription(description) } />
                </Card>
            </StyledBookPreview>
        );
    }
}

const StyledBookPreview = styled.div`
    display: inline-block;
    margin: 10px 0;
    position: relative;

    .preview-card {
        height: 340px;
    }

    .ant-card-cover {
        height: 146.56px;
    }

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