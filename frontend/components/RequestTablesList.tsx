import styles from "../styles/Home.module.css";
import React, { useState } from "react";
import { IRequestTable } from "../common/models/IRequestTable";
import { TrashIcon } from "@heroicons/react/24/solid";

interface IRequestTablesListProps {
  tables: IRequestTable[];
  clearAllTables: () => void;
  removeTable: (table: IRequestTable) => void;
}

const RequestTablesList = ({requestTables, clearAllTables, removeTable}) => {
  // const [activeTable, setActiveTable] = useState<IRequestTable>(undefined);

  // const handleClick = () => {};

  // const handleClear = () => {
  //   localStorage.setItem("requestTables", JSON.stringify([]));
  //   window.location.reload();
  // }

  // const removeTable = (table: IRequestTable) => {
  //   const newTables = tables.filter((t) => t.name !== table.name);
  //   localStorage.setItem("requestTables", JSON.stringify(newTables));
  //   window.location.reload();
  // }

  return requestTables.length === 0 ? null : (
    <div className={styles.requestTablesListWrapper}>
      <h2>Request classes:</h2>
      <div 
        className={styles.displayResultTablesClearPanel} 
        onClick={() => clearAllTables()}
      >
        {"Clear all tables "}
        <TrashIcon
              className={styles.recordXButton}
            />
      </div>
      
      {requestTables.map((table) => (
        <div
          className={styles.requestTablesListItem}
          // onClick={handleClick}
        >
          <div>
          <h3>{table.name}</h3>
          <div>{`Class has ${table.fields.length} attribute`}</div>
          </div>
          <TrashIcon className={styles.recordXButton} onClick={()=>removeTable(table)}/>
        </div>
      ))}
    </div>
  );
};

export default RequestTablesList;
