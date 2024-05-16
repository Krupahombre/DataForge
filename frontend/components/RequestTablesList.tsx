import styles from "../styles/Home.module.css";
import React, { useState } from "react";
import { IRequestTable } from "../common/models/IRequestTable";

const RequestTablesList = (props) => {
  const tables: IRequestTable[] = props.requestTables;
  // const [activeTable, setActiveTable] = useState<IRequestTable>(undefined);

  // const handleClick = () => {};

  return tables.length === 0 ? null : (
    <div className={styles.requestTablesListWrapper}>
      <h2>Request classes:</h2>
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
