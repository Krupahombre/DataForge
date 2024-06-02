import styles from "../styles/Home.module.css";
import React from "react";
import { IRequestTable } from "../common/models/IRequestTable";
import { TrashIcon } from "@heroicons/react/24/solid";

interface IRequestTablesListProps {
  requestTables: IRequestTable[];
  clearAllTables: () => void;
  removeTable: (table: IRequestTable) => void;
}

const RequestTablesList: React.FC<IRequestTablesListProps> = (props) => {
  const { requestTables, clearAllTables, removeTable } = props;

  return requestTables.length === 0 ? null : (
    <div className={styles.requestTablesListWrapper}>
      <h2>{"Your tables:"}</h2>
      <div
        className={styles.displayResultTablesClearPanel}
        onClick={() => clearAllTables()}
      >
        {"Clear all tables "}
        <TrashIcon className={styles.recordXButton} />
      </div>

      {requestTables.map((table, key) => (
        <div className={styles.requestTablesListItem} key={key}>
          <div>
            <h3>{table.name}</h3>
            <div>{`Class has ${table.fields.length} attribute${
              table.fields.length > 1 ? "s" : ""
            }`}</div>
          </div>
          <TrashIcon
            className={styles.recordXButton}
            onClick={() => removeTable(table)}
          />
        </div>
      ))}
    </div>
  );
};

export default RequestTablesList;
