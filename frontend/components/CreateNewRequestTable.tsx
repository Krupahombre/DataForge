import React, { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";
import {
  IRequestTable,
  IResultTableRecord,
} from "../common/models/IRequestTable";
import Dropdown from "react-bootstrap/Dropdown";
import "bootstrap/dist/css/bootstrap.min.css";
import { TrashIcon } from "@heroicons/react/24/solid";
import { IProductClass } from "../common/models/IProductClass";

const defaultTable: IRequestTable = {
  name: "",
  fields: [],
};

const defaultResultTableRecord: IResultTableRecord = {
  name: "",
  type: "",
  subtype: "",
};

const CreateNewRequestTable = (props) => {
  const { productClasses, addTable } = props;
  const [resultTable, setResultTable] = useState<IRequestTable>(defaultTable);

  const [resultTableRecord, setResultTableRecord] =
    useState<IResultTableRecord>(defaultResultTableRecord);

  useEffect(() => {
    onSelectedSubtype("");
  }, [resultTableRecord.type]);

  const onSubmitNewTable = () => {
    if (resultTable.name === "" || resultTable.fields.length === 0) return;
    addTable(resultTable);
    setResultTable(defaultTable);
    setResultTableRecord(defaultResultTableRecord);
  };

  const onTableNameChange = (name: string) => {
    setResultTable({ ...resultTable, name });
  };

  const onSelectedType = (type: string) => {
    setResultTableRecord({ ...resultTableRecord, type });
  };

  const onSelectedSubtype = (subtype: string) => {
    setResultTableRecord({ ...resultTableRecord, subtype });
  };

  const addAllSubtypes = () => {
    const productClass:IProductClass = productClasses.find((productClass)=> productClass.name === resultTableRecord.type);
    const records:IResultTableRecord[] = productClass.fields.map((field) => ({
      name: field,
      type: resultTableRecord.type,
      subtype: field,
    }));
    
    setResultTable({ ...resultTable, fields: [...resultTable.fields, ...records] })
    onSelectedType("");
  }

  const onChangedName = (name: string) => {
    setResultTableRecord({ ...resultTableRecord, name });
  };

  const addNewRecord = () => {
    if (
      resultTableRecord.name === "" ||
      resultTableRecord.type === "" ||
      resultTableRecord.subtype === ""
    )
      return;
    setResultTable({
      ...resultTable,
      fields: [...resultTable.fields, resultTableRecord],
    });
    setResultTableRecord(defaultResultTableRecord);
  };

  const handleRemoveField = (index) => {
    const updatedFields = resultTable.fields.filter((_, i) => i !== index);
    setResultTable({ ...resultTable, fields: updatedFields });
  };

  const getSubtypesArray = () => {
    if (!resultTableRecord.type) return [];
    return productClasses.find(
      (productClass) => productClass.name === resultTableRecord.type
    ).fields;
  };

  return (
    <div className={styles.wymyslyKleksa}>
      <div className={styles.tablenameInputWrapper}>
        {"Your Table Name:"}
        <input
          className={styles.tableNameInput}
          placeholder="Fill table name"
          type="text"
          value={resultTable.name}
          onChange={(e) => onTableNameChange(e.target.value)}
        />
      </div>
      <div className={styles.createNewRequestTableWrapper}>
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
        <div className={styles.newRecordWrapper}>
          <input
            placeholder="Fill row name"
            className={styles.newRequestRecordNameInput}
            type="text"
            onChange={(e) => onChangedName(e.target.value)}
            value={resultTableRecord.name}
          />

          <Dropdown className={styles.newRecordWrapperDropdown}>
            <Dropdown.Toggle variant="success" id="dropdown-basic">
              {resultTableRecord.type ? resultTableRecord.type : "Choose type"}
            </Dropdown.Toggle>

            <Dropdown.Menu>
              {productClasses.map((productClass, key) => (
                <Dropdown.Item
                  key={key}
                  onClick={() => onSelectedType(productClass.name)}
                >
                  {productClass.name}
                </Dropdown.Item>
              ))}
            </Dropdown.Menu>
          </Dropdown>

          {resultTableRecord.type && (
            <Dropdown className={styles.newRecordWrapperDropdown}>
              <Dropdown.Toggle variant="success" id="dropdown-basic">
                {resultTableRecord.subtype
                  ? resultTableRecord.subtype
                  : "Choose subtype"}
              </Dropdown.Toggle>

              <Dropdown.Menu>
                {getSubtypesArray().map((productClass, key) => (
                  <Dropdown.Item
                    key={key}
                    onClick={() => onSelectedSubtype(productClass)}
                  >
                    {productClass}
                  </Dropdown.Item>
                ))}
                <Dropdown.Item onClick={() => addAllSubtypes()}>
                  {"Add all"}
                </Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>
          )}
          {resultTableRecord.type && resultTableRecord.subtype && (
            <button
              type="button"
              className={styles.newRecordAddBtn + " btn btn-dark"}
              onClick={addNewRecord}
            >
              Add
            </button>
          )}
        </div>
        <div className={styles.newRequestSubmitBtnWrapper}></div>
      </div>
      <button
        type="button"
        className={styles.newRequestSubmitBtn + " btn-dark"}
        onClick={onSubmitNewTable}
      >
        ➕
      </button>
    </div>
  );
};

export default CreateNewRequestTable;
