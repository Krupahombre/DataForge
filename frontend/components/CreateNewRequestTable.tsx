import React, { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";
import {
  IRequestTable,
  IResultTableRecord,
} from "../common/models/IRequestTable";
import Dropdown from "react-bootstrap/Dropdown";
import "bootstrap/dist/css/bootstrap.min.css";

const defaultTable: IRequestTable = {
  name: "",
  fields: [
    {
      name: "Name",
      type: "person",
      subtype: "name",
    },
    {
      name: "LastName",
      type: "person",
      subtype: "lastname",
    },
  ],
};

const defaultResultTableRecord: IResultTableRecord = {
  name: "",
  type: "",
  subtype: "",
};

const CreateNewRequestTable = (props) => {
  const { productClasses, setTables } = props;
  const [resultTable, setResultTable] = useState<IRequestTable>(defaultTable);

  const [resultTableRecord, setResultTableRecord] =
    useState<IResultTableRecord>(defaultResultTableRecord);

  useEffect(() => {
    onSelectedSubtype("");
  }, [resultTableRecord.type]);

  const onTableNameChange = (name: string) => {
    setResultTable({ ...resultTable, name });
  };

  const onSelectedType = (type: string) => {
    setResultTableRecord({ ...resultTableRecord, type });
  };

  const onSelectedSubtype = (subtype: string) => {
    setResultTableRecord({ ...resultTableRecord, subtype });
  };

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
    <div className={styles.createNewRequestTableWrapper}>
      <input
        type="text"
        value={resultTable.name}
        onChange={(e) => onTableNameChange(e.target.value)}
      />
      {resultTable.fields.map((field, key) => (
        <div className={styles.createNewRequestRecord}>
          <div>
            <button
              className={styles.recordXButton}
              onClick={() => handleRemoveField(key)}
            >
              x
            </button>
          </div>
          <div className={styles.recordName}>{field.name}</div>
          <div>{"from"}</div>
          <div className={styles.recordDetails}>{field.type}</div>
          <div>{">"}</div>
          <div className={styles.recordDetails}>{field.subtype}</div>
        </div>
      ))}
      <div className={styles.newRecordWrapper}>
        <button className={styles.recordXButton} onClick={addNewRecord}>
          +
        </button>
        <input
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
          <Dropdown>
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
            </Dropdown.Menu>
          </Dropdown>
        )}
      </div>
      {/* <button onClick={}>Add new table</button> */}
    </div>
  );
};

export default CreateNewRequestTable;
