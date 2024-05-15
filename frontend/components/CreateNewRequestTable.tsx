import React, { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";
import {
  IRequestTable,
  IResultTableRecord,
} from "../common/models/IRequestTable";
import Dropdown from "react-bootstrap/Dropdown";
import "bootstrap/dist/css/bootstrap.min.css";

const defaultTable: IRequestTable = {
  name: "Person",
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
  const [newResultTable, setNewResultTable] =
    useState<IRequestTable>(defaultTable);

  const [newResultTableRecord, setNewResultTableRecord] =
    useState<IResultTableRecord>(defaultResultTableRecord);

  useEffect(() => {
    onSelectedSubtype("");
  }, [newResultTableRecord.type]);

  const onSelectedType = (type: string) => {
    setNewResultTableRecord({ ...newResultTableRecord, type });
  };

  const onSelectedSubtype = (subtype: string) => {
    setNewResultTableRecord({ ...newResultTableRecord, subtype });
  };

  const getSubtypesArray = () => {
    if (!newResultTableRecord.type) return [];
    return productClasses.find(
      (productClass) => productClass.name === newResultTableRecord.type
    ).fields;
  };

  return (
    <div className={styles.createNewRequestTableWrapper}>
      {newResultTable.fields.map((field, key) => (
        <div className={styles.createNewRequestRecord}>
          <div>
            <button className={styles.recordXButton}>x</button>
          </div>
          <div className={styles.recordName}>{field.name}</div>
          <div>{"from"}</div>
          <div className={styles.recordDetails}>{field.type}</div>
          <div>{">"}</div>
          <div className={styles.recordDetails}>{field.subtype}</div>
        </div>
      ))}
      <div className={styles.newRecordWrapper}>
        <button className={styles.recordXButton}>+</button>
        <input className={styles.newRequestRecordNameInput} type="text" />

        <Dropdown className={styles.newRecordWrapperDropdown}>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            {newResultTableRecord.type
              ? newResultTableRecord.type
              : "Choose type"}
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

        {newResultTableRecord.type && (
          <Dropdown>
            <Dropdown.Toggle variant="success" id="dropdown-basic">
              {newResultTableRecord.subtype
                ? newResultTableRecord.subtype
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
    </div>
  );
};

export default CreateNewRequestTable;
