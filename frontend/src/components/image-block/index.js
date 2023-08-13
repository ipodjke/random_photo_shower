function ImageBox(url) {
    return (
      <div>
        <img src={process.env.REACT_APP_IMG_URL + url.url}/>
      </div>
    )
  }

export default ImageBox;