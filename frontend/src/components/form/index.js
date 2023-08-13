import { useEffect, useState } from 'react';
import axios from 'axios';
import Button from 'react-bootstrap/Button';

import Checkbox from '../checkbox';


function ImageForm({setImageUrl}) {
  const ApiUrl = process.env.REACT_APP_API_URL
  const [tags, setTags] = useState(null)

  // костыль реализация, к сожалению.
  useEffect(() => {
    axios.get(ApiUrl + '/tags/')
    .then((response) => {
      setTags(response.data)
    }).catch((error) => {
      console.log(error)
    });
  });

  function onSubmit(e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);    
    const formJson = Object.fromEntries(formData.entries());
    const params = new URLSearchParams();
    Object.keys(formJson).map((key) => {
      params.append('category', key)
    })
    
    axios.get(ApiUrl + '/photo/', {params: params})
    .then((res) => {
      setImageUrl(res.data.image)
    }).catch((error) => {
      console.log(error)
    });
  }

  return (
    <form onSubmit={onSubmit}>
      {tags &&
        tags.map((tags) => {
          return <Checkbox name={tags.slug} key={tags.id}/>
        })
      }
      <div>
        <Button variant="success" type="submit">
          Показать
        </Button>
      </div>
    </form>
  );
}
  
export default ImageForm;