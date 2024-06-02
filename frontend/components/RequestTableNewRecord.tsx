import React from "react";
import styles from "../styles/Home.module.css";
import Dropdown from "react-bootstrap/Dropdown";
import "bootstrap/dist/css/bootstrap.min.css";
import { IProductClass } from "../common/models/IProductClass";
import { IResultTableRecord } from "../common/models/IRequestTable";
import { IRequestTable } from "../common/models/IRequestTable";
import { IErrors } from "../common/models/IErrors";
import { defaultResultTableRecord } from "../common/models/IRequestTable";

interface IRequestTableNewRecordProps {
  productClasses: IProductClass[];
  resultTable: IRequestTable;
  setResultTable: (table: IRequestTable) => void;
  resultTableRecord: IResultTableRecord;
  setResultTableRecord: (record: IResultTableRecord) => void;
  error: IErrors;
  setError: (error: IErrors) => void;
  onSelectedSubtype: (subtype: string) => void;
}

const RequestTableNewRecord: React.FC<IRequestTableNewRecordProps> = (
  props
) => {
  const {
    productClasses,
    resultTable,
    setResultTable,
    resultTableRecord,
    setResultTableRecord,
    error,
    setError,
    onSelectedSubtype,
  } = props;

  const areAllSubtypesAdded = () => {
    const productClass: IProductClass = productClasses.find(
      (productClass) => productClass.name === resultTableRecord.type
    );
    return productClass.fields.every((field) =>
      isAlreadyAdded(resultTableRecord.type, field)
    );
  };

  const addAllSubtypes = () => {
    const productClass: IProductClass = productClasses.find(
      (productClass) => productClass.name === resultTableRecord.type
    );
    const records: IResultTableRecord[] = productClass.fields
      .filter((field) => !isAlreadyAdded(resultTableRecord.type, field))
      .map((field) => ({
        name: field,
        type: resultTableRecord.type,
        subtype: field,
      }));

    setResultTable({
      ...resultTable,
      fields: [...resultTable.fields, ...records],
    });
    onSelectedType("");
  };

  const onChangedName = (name: string) => {
    setResultTableRecord({ ...resultTableRecord, name });
  };

  const getSubtypesArray = () => {
    if (!resultTableRecord.type) return [];
    return productClasses.find(
      (productClass) => productClass.name === resultTableRecord.type
    ).fields;
  };

  const addNewRecord = () => {
    if (
      resultTableRecord.name === "" ||
      resultTableRecord.type === "" ||
      resultTableRecord.subtype === ""
    ) {
      setError({ ...error, recordNameError: true });
      return;
    }
    setResultTable({
      ...resultTable,
      fields: [...resultTable.fields, resultTableRecord],
    });
    setResultTableRecord(defaultResultTableRecord);
    setError({ ...error, recordNameError: false });
  };

  const onSelectedType = (type: string) => {
    setResultTableRecord({ ...resultTableRecord, type });
  };

  const isAlreadyAdded = (type: string, subtype: string) => {
    return resultTable.fields.some(
      (field) => field.type === type && field.subtype === subtype
    );
  };

  return (
    <div className={styles.newRecordWrapper}>
      <input
        placeholder="Fill row name"
        className={styles.newRequestRecordNameInput}
        type="text"
        onChange={(e) => onChangedName(e.target.value)}
        value={resultTableRecord.name}
        style={error.recordNameError ? { border: "1px solid red" } : {}}
      />

      <Dropdown className={styles.newRecordWrapperDropdown}>
        <Dropdown.Toggle id="dropdown-basic" className={styles.dropdown}>
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
          <Dropdown.Toggle id="dropdown-basic" className={styles.dropdown}>
            {resultTableRecord.subtype
              ? resultTableRecord.subtype
              : "Choose subtype"}
          </Dropdown.Toggle>

          <Dropdown.Menu>
            {getSubtypesArray().map((productClass, key) => (
              <Dropdown.Item
                key={key}
                onClick={() => onSelectedSubtype(productClass)}
                style={
                  isAlreadyAdded(resultTableRecord.type, productClass)
                    ? { display: "none" }
                    : {}
                }
              >
                {productClass}
              </Dropdown.Item>
            ))}
            {areAllSubtypesAdded() ? (
              <Dropdown.Item disabled>All fields added</Dropdown.Item>
            ) : (
              <Dropdown.Item onClick={() => addAllSubtypes()}>
                Add all
              </Dropdown.Item>
            )}
          </Dropdown.Menu>
        </Dropdown>
      )}
      {resultTableRecord.type && resultTableRecord.subtype && (
        <button
          type="button"
          className={styles.newRecordAddBtn}
          onClick={addNewRecord}
        >
          Add
        </button>
      )}
    </div>
  );
};

export default RequestTableNewRecord;
