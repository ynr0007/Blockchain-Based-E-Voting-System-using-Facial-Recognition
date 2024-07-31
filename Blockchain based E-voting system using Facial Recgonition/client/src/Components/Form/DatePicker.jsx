import React from "react";

const DatePicker = (props) => {
  const max = "2001-08-13";
  return (
    <div style={{ display: "flex", justifyContent: "space-between" }}>
      <label>{props.title}</label>&nbsp;
      <input type="date" name={props.name} max={max} />
    </div>
  );
};

export default DatePicker;
