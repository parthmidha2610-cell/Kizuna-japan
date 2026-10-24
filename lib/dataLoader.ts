// lib/dataLoader.ts
import { collection, getDocs } from 'firebase/firestore';
import { db } from './firebase';
import { CatalogTitle } from '../types/catalog';

export async function fetchFullCatalog(): Promise<CatalogTitle[]> {
  try {
    const catalogCol = collection(db, 'catalog');
    const snapshot = await getDocs(catalogCol);
    return snapshot.docs.map(doc => doc.data() as CatalogTitle);
  } catch (error) {
    console.error("Firebase fetch error:", error);
    return []; 
  }
}