import React from 'react';
import styled from 'styled-components';

export default class Categories extends React.Component {
    render(){
        return (
            <StyledCategories>
                <span> <a className='science'>科普</a> <a className='computer'>计算机    </a> <a className='literature'>文学</a>  <a className='history'>历史</a> <a className='agriculture'>农业</a> <a className='industry'>工业</a> </span>
            </StyledCategories>
        );
    }
}

const StyledCategories = styled.div`
    height: 34px;
    background: #f9f9f9;
    margin-left:50px;
    padding: 0px,15px;
    * {
        font-size: 12px;
        line-height: 33px;
        display: flex;
        flex-wrap: wrap;
        
        justify-content:space-around;
        
    }

    a.science {
        color: black;
        &:hover{
            color:red;
        }
    }
    a.computer {
        color: black;
        &:hover {
            color: red;
        }
    }
    a.literature {
        color: black;
        &:hover {
            color: red;
        }
    }
    a.history {
        color: black;
        &:hover {
            color: red;
        }
    }
    a.agriculture {
        color: black;
        &:hover {
            color: red;
        }
    }
    a.industry {
        color: black;
        &:hover {
            color: red;
        }
    }
`;