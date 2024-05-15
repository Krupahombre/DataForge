import styles from "../styles/Home.module.css";

import React from "react";
const RequestTablesList = (props) => {
  const tables = props.requestTables;
  return (
    <div>
      {tables.map((table) => (
        <div className={styles.squareBox}>{table.name}</div>
      ))}
    </div>
  );
};

export default RequestTablesList;
