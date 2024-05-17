import React, { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";
import FormatFilters from "../components/FormatFilters";
import TypeFilters from "../components/TypeFilters";
import IFilter from "../common/models/IFilter";
import { IRequestTable } from "../common/models/IRequestTable";
import { IProductClass } from "../common/models/IProductClass";
import type { NextPage } from "next";
import { useRouter } from "next/router";
import RequestTablesList from "../components/RequestTablesList";
import CreateNewRequestTable from "../components/CreateNewRequestTable";
import { getProductClasses } from "../common/services/getProductClasses";

const defaultProductClasses: IProductClass[] = [];

const getFormat = (): IFilter[] => {
  return [
    { name: "JSON", selected: false },
    { name: "MySQL", selected: false },
    { name: "PSQL", selected: false}
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

  const router = useRouter();

  const handleGenerate = () => {
    if (isFormFilled()) {
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

  const isFormFilled = () => {
    return (
      formatFilters.some((column) => column.selected) &&
      requestTables.length > 0
    );
  };

  const addTable = (newTable: IRequestTable) => {
    localStorage.setItem("requestTables", JSON.stringify([...requestTables, newTable]));
    setRequestTables([...requestTables, newTable]);
  };

  return (
    <div className={styles.dataForge}>
      <div className={styles.heroBox}>
        <div>
          <h1 className={styles.heroLabel}>Data Forge</h1>
          <h2 className={styles.heroSubLabel}>Generate your data!</h2>
        </div>
        <div>
          <div className={styles.userInputWrapper}>
            <CreateNewRequestTable
              productClasses={productClasses}
              addTable={addTable}
            />
            <RequestTablesList requestTables={requestTables} />
          </div>
        </div>

        <div className={styles.generateButtonBox}>
          <FormatFilters
            filters={formatFilters}
            setFilters={setFormatFilters}
          />
          <button onClick={handleGenerate} className={styles.generateButton}>
            Generate
          </button>
        </div>
      </div>
    </div>
  );
};
export default HeroPage;
