import React, { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";
import {
  IRequestTable,
  IResultTableRecord,
} from "../common/models/IRequestTable";
import "bootstrap/dist/css/bootstrap.min.css";
import { TrashIcon } from "@heroicons/react/24/solid";
import { IErrors, defaultErrors } from "../common/models/IErrors";
import RequestTableNewRecord from "./RequestTableNewRecord";
import {
  defaultTable,
  defaultResultTableRecord,
} from "../common/models/IRequestTable";
import { IProductClass } from "../common/models/IProductClass";

interface ICreateNewRequestTableProps {
  productClasses: IProductClass[];
  addTable: (table: IRequestTable) => void;
}

const CreateNewRequestTable: React.FC<ICreateNewRequestTableProps> = (
  props
) => {
  const { productClasses, addTable } = props;
  const [error, setError] = useState<IErrors>(defaultErrors);
  const [resultTable, setResultTable] = useState<IRequestTable>(defaultTable);

  const [resultTableRecord, setResultTableRecord] =
    useState<IResultTableRecord>(defaultResultTableRecord);

  useEffect(() => {
    onSelectedSubtype("");
  }, [resultTableRecord.type]);

  const onSubmitNewTable = () => {
    if (resultTable.name === "" || resultTable.fields.length === 0) {
      setError({
        ...error,
        tableNameError: resultTable.name === "",
        noListItemsError: resultTable.fields.length === 0,
      });
      return;
    }

    addTable(resultTable);
    setResultTable(defaultTable);
    setResultTableRecord(defaultResultTableRecord);
    setError(defaultErrors);
  };

  const onTableNameChange = (name: string) => {
    setResultTable({ ...resultTable, name });
  };

  const onSelectedSubtype = (subtype: string) => {
    setResultTableRecord({ ...resultTableRecord, subtype });
  };

  const handleRemoveField = (index: number) => {
    const updatedFields = resultTable.fields.filter((_, i) => i !== index);
    setResultTable({ ...resultTable, fields: updatedFields });
  };

  return (
    <div className={styles.wymyslyKleksa}>
      <div className={styles.tablenameInputWrapper}>
        <h2>{"New table:"}</h2>
        <input
          className={styles.tableNameInput}
          placeholder="Fill table name"
          type="text"
          value={resultTable.name}
          onChange={(e) => onTableNameChange(e.target.value)}
          style={error.tableNameError ? { border: "1px solid red" } : {}}
        />
      </div>
      <div
        className={styles.createNewRequestTableWrapper}
        style={error.noListItemsError ? { border: "1px solid red" } : {}}
      >
        {resultTable.fields.map((field, key) => (
          <div className={styles.createNewRequestRecord}>
            <TrashIcon
              onClick={() => handleRemoveField(key)}
              className={styles.recordXButton}
            />
            <div className={styles.recordName}>{field.name}</div>
            <div>{"from"}</div>
            <div className={styles.recordDetails}>{field.type}</div>
            <div>{">"}</div>
            <div className={styles.recordDetails}>{field.subtype}</div>
          </div>
        ))}
        <RequestTableNewRecord
          productClasses={productClasses}
          resultTable={resultTable}
          setResultTable={setResultTable}
          resultTableRecord={resultTableRecord}
          setResultTableRecord={setResultTableRecord}
          error={error}
          setError={setError}
          onSelectedSubtype={onSelectedSubtype}
        />
        <div className={styles.newRequestSubmitBtnWrapper}></div>
      </div>
      <button className={styles.newRequestSubmitBtn} onClick={onSubmitNewTable}>
        ➕
      </button>
    </div>
  );
};

export default CreateNewRequestTable;
