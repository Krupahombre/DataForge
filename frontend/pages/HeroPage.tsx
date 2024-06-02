import React, { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";
import FormatFilters from "../components/FormatFilters";
import IFilter from "../common/models/IFilter";
import { IRequestTable } from "../common/models/IRequestTable";
import { IProductClass } from "../common/models/IProductClass";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import RequestTablesList from "../components/RequestTablesList";
import CreateNewRequestTable from "../components/CreateNewRequestTable";
import { getProductClasses } from "../common/services/getProductClasses";
import "bootstrap/dist/css/bootstrap.min.css";
import NavBar from "../components/NavBar";

const defaultProductClasses: IProductClass[] = [];

const getFormat = (): IFilter[] => {
  return [
    { name: "JSON", selected: false },
    { name: "MySQL", selected: false },
    { name: "PSQL", selected: false },
  ];
};

const HeroPage: NextPage = () => {
  const [formatFilters, setFormatFilters] = useState<IFilter[]>(
    [] as IFilter[]
  );
  const [requestTables, setRequestTables] = useState<IRequestTable[]>(
    [] as IRequestTable[]
  );
  const [productClasses, setProductClasses] = useState<IProductClass[]>(
    defaultProductClasses
  );
  const [numberOfRecords, setNumberOfRecords] = useState<number>(10);

  const router = useRouter();

  const handleGenerate = () => {
    if (isFormFilled()) {
      localStorage.setItem("numberOfRecords", JSON.stringify(numberOfRecords));
      localStorage.setItem("requestTables", JSON.stringify(requestTables));
      localStorage.setItem(
        "formatFilters",
        JSON.stringify(formatFilters.find((column) => column.selected).name)
      );
      router.push(`/ResultDisplayPage`);
    } else {
      alert("Please create at least one table and select a format!");
    }
  };

  useEffect(() => {
    const stringRequestTables = localStorage.getItem("requestTables");
    if (stringRequestTables) {
      setRequestTables(JSON.parse(stringRequestTables));
    }
    getProductClasses().then((data) => {
      setProductClasses(data);
    });
    setFormatFilters(getFormat());
  }, []);

  const updateNumberOfRecords = (number: number) => {
    if (number < 1) {
      return setNumberOfRecords(1);
    }
    if (number > 9999999) {
      return setNumberOfRecords(9999999);
    }
    setNumberOfRecords(number);
  };

  const isFormFilled = () => {
    return (
      formatFilters.some((column) => column.selected) &&
      requestTables.length > 0
    );
  };

  const addTable = (newTable: IRequestTable) => {
    localStorage.setItem(
      "requestTables",
      JSON.stringify([...requestTables, newTable])
    );
    setRequestTables([...requestTables, newTable]);
  };

  const removeTable = (table: IRequestTable) => {
    const newTables = requestTables.filter((t) => t.name !== table.name);
    setRequestTables(newTables);
    localStorage.setItem("requestTables", JSON.stringify(newTables));
  };

  const clearAllTables = () => {
    localStorage.setItem("requestTables", JSON.stringify([]));
    setRequestTables([]);
  };

  return (
    <div className={styles.dataForge}>
      <NavBar />
      <div className={styles.heroBox}>
        <div className={styles.userInputWrapper}>
          <CreateNewRequestTable
            productClasses={productClasses}
            addTable={addTable}
          />
          <RequestTablesList
            requestTables={requestTables}
            clearAllTables={clearAllTables}
            removeTable={removeTable}
          />
        </div>

        <FormatFilters
          filters={formatFilters}
          setFilters={setFormatFilters}
          handleGenerate={handleGenerate}
          numberOfRecords={numberOfRecords}
          setNumberOfRecords={updateNumberOfRecords}
        />
      </div>
    </div>
  );
};
export default HeroPage;
