
function Checkbox(name) {
    return (
      <div className='checkbox'>
        <label>
          {name.name}
          <input
            name={name.name}
            type="checkbox"
            defaultChecked={true}
          />
        </label>
      </div>
    );
  }

  export default Checkbox;