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

const defaultProductClasses: IProductClass[] = [
  {
    name: "Person",
    fields: ["name", "surname", "age", "email"],
  },
  {
    name: "IBAN",
    fields: ["iban", "country", "bank"],
  },
];

const getTypes = (): IFilter[] => {
  return [
    { name: "person", selected: false },
    { name: "iban", selected: false },
  ];
};

const getFormat = (): IFilter[] => {
  return [
    { name: "JSON", selected: false },
    { name: "MySQL", selected: false },
  ];
};

const HeroPage: NextPage = () => {
  const [formatFilters, setFormatFilters] = useState<IFilter[]>(
    [] as IFilter[]
  );
  const [typeFilters, setTypeFilters] = useState<IFilter[]>([] as IFilter[]);
  const [requestTables, setRequestTables] = useState<IRequestTable[]>(
    [] as IRequestTable[]
  );
  const [productClasses, setProductClasses] = useState<IProductClass[]>(
    defaultProductClasses
  );

  const router = useRouter();

  const handleGenerate = () => {
    const type = typeFilters.filter((column) => column.selected);
    const format = formatFilters.find((type) => type.selected)?.name;

    if (isFormFilled()) {
      const queryString =
        `a=b&format=${format}&` +
        type.map((value) => `type=${value.name}`).join("&");
      router.push(`/ResultDisplayPage?${queryString}`);
    }
  };

  useEffect(() => {
    setFormatFilters(getFormat());
    setTypeFilters(getTypes());
  }, []);

  const isFormFilled = () => {
    return (
      formatFilters.some((column) => column.selected) &&
      typeFilters.some((type) => type.selected)
    );
  };

  const addTable = (newTable: IRequestTable) => {
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
