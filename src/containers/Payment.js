import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { PUBLIC_URL } from '../constants';
import { List, Avatar, Button, Skeleton, InputNumber } from 'antd';
import './Payment.css';
import { randomNonNegativeNumber } from '../utils';
import { sliceString } from '../utils';

export default class Cart extends React.Component {
    state = {
        initLoading: true,
        loading: false,
        list: [],
        totalPrice: 0
    }

    async componentDidMount() {
        const res = await fetch(`${PUBLIC_URL}/mock/booklist.json`);
        const data = await res.json();
        const list = [];

        // This code not works.
        for (let i = 0; i < 5; i++) {
            const index = randomNonNegativeNumber(20);
            if (!list.includes(index)) {
                list.push(data[index]);
            }
        }

        this.setState({
            initLoading: false,
            list: list,
        });

        let totalPrice = 0;
        const singlePrices = document.querySelectorAll('.single-book-price');
        singlePrices.forEach(ele => {
            const price = parseFloat(ele.innerHTML.replace('￥',''));
            const count = ele.parentNode.nextSibling.querySelector('input').value;
            totalPrice += price * count;
        });
        this.setState({ totalPrice: totalPrice });
    }

    render() {
        const { initLoading, list } = this.state;

        return (
            <React.Fragment>
                <h1 className='markdown h1'>确认订单</h1>
                <List
                    className='order-list-header'
                    loading={initLoading}
                    itemLayout="horizontal"
                    dataSource={[{ price: 12, description: '', cover: '', loading: false }]}
                    renderItem={({ price, description, cover, loading }) => (
                        <List.Item
                            actions={[
                                <span style={ { marginLeft: -60, padding: 0 } }>封面</span>,
                                <b style={ { padding: '10px 38px' } }>图书名</b>,
                                <span style={ { padding: '10px 242px' } }>图书描述</span>,
                                <span style={ { padding: '10px 25px' } }>单价</span>,
                                <span style={ { padding: '10px 16px' } }>购买数量</span>,
                                <span>操作</span>
                            ]}
                        >
                        </List.Item>
                    )}
                />
                <List
                    className='order-list'
                    loading={initLoading}
                    itemLayout="horizontal"
                    dataSource={list}
                    renderItem={({ name, price, cover, loading, description }) => (
                        <List.Item
                            actions={[
                                <span style={ { marginLeft: 0, width: 1000 } }>{ sliceString(description, 30) }</span>,
                                <span style={{ width: 80, display: 'inline-block' }} class='single-book-price'>￥{price}</span>,
                                <InputNumber
                                    className='order-num'
                                    size="small" min={1}
                                    max={100000}
                                    defaultValue={randomNonNegativeNumber(10)}
                                    id={'order-book-number'}
                                />,
                                <a>移除</a>
                            ]}
                        >
                            <Skeleton avatar title={true} loading={loading} active>
                                <List.Item.Meta
                                    avatar={
                                        <Avatar src={cover} shape='square' />
                                    }
                                    description={name}
                                />
                            </Skeleton>
                        </List.Item>
                    )}
                />
                <div style={ { position: 'relative' } }>
                    <span style={{ position: 'absolute', right: 450, fontSize: 24 }}>总价: ￥{ this.state.totalPrice }</span>
                    <Button style={{ position: 'absolute', right: 350 }}>确认付款</Button>
                </div>
            </React.Fragment>
        );
    }
}

