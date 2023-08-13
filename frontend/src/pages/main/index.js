import { useState } from "react";
import { Container, Row, Col } from "react-bootstrap";

import ImageForm from "../../components/form";
import ImageBox from "../../components/image-block";


function HomePpage() {
    const [imageUrl, setImageUrl] = useState(null)

    return (
     <Container>
        <Row>
            <Col>
              <h1>Сервис показа случайных картинок по выбраным тегам</h1>
              <h3>Выберите категории для показа картинки</h3>
            </Col>
        </Row>
        <Row>
            <Col>
              <ImageForm setImageUrl={setImageUrl} />
            </Col>
        </Row>
        {imageUrl && 
          <Row>
            <Col>
                <ImageBox url={imageUrl}/>
            </Col>
          </Row>
        }
      </Container>
    );
  }
  
  export default HomePpage;