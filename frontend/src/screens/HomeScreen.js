import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Row, Col } from 'react-bootstrap';
import Product from '../components/Product';
import Loader from '../components/Loader';
import Message from '../components/Message';
import Paginate from '../components/Paginate';
import ProductCarousel from '../components/ProductCarousel';
import { listProducts } from '../actions/productActions';

import axios from 'axios';

const HomeScreen = ({ history }) => {
  //const dispatch = useDispatch();
  //const productList = useSelector((state) => state.productList);
  //const { error, loading, products, page, pages } = productList;

  //let keyword = history.location.search;

  //useEffect(() => {
  //  dispatch(listProducts(keyword));
  //}, [dispatch, keyword]);

  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProd = async () => {
      // no write the entire url because the other part of the url is in proxy packajge.json
      const { data } = await axios.get('/api/products/');
      setProducts(data);
    };

    fetchProd();
  }, []);

  return (
    <div>
      <h1>Latest Products</h1>
      <div>
        <Row>
          {products.map((product) => (
            <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
              <Product product={product} />
            </Col>
          ))}
        </Row>
      </div>
    </div>
  );
};

export default HomeScreen;
