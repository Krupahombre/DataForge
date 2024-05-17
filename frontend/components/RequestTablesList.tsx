import styles from "../styles/Home.module.css";
import React, { useState } from "react";
import { IRequestTable } from "../common/models/IRequestTable";
import { TrashIcon } from "@heroicons/react/24/solid";

const RequestTablesList = (props) => {
  const tables: IRequestTable[] = props.requestTables;
  // const [activeTable, setActiveTable] = useState<IRequestTable>(undefined);

  // const handleClick = () => {};

  const handleClear = () => {
    localStorage.setItem("requestTables", JSON.stringify([]));
    window.location.reload();
  }

  return tables.length === 0 ? null : (
    <div className={styles.requestTablesListWrapper}>
      <h2>Request classes:</h2>
      <div 
        className={styles.displayResultTablesClearPanel} 
        onClick={() => handleClear()}
      >
        {"Clear all tables "}
        <TrashIcon
              className={styles.recordXButton}
            />
      </div>
      
      {tables.map((table) => (
        <div
          className={styles.requestTablesListItem}
          // onClick={handleClick}
        >
          <h3>{table.name}</h3>
          <div>{`Class has ${table.fields.length} attribute`}</div>
        </div>
      ))}
    </div>
  );
};

export default RequestTablesList;
