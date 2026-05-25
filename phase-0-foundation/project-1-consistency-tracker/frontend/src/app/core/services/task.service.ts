import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Task } from '../models/task.model';

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  private apiUrl = 'http://127.0.0.1:8000/tasks';

  constructor(private http: HttpClient) {}

  private getHeaders() {
    const token = localStorage.getItem('token');

    return {
      headers: new HttpHeaders({
        Authorization: `Bearer ${token}`
      })
    };
  }

  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(
      `${this.apiUrl}/`,
      this.getHeaders()
    );
  }

  createTask(task: any): Observable<Task> {
    return this.http.post<Task>(
      `${this.apiUrl}/`,
      task,
      this.getHeaders()
    );
  }

  updateTask(id: number, task: any): Observable<Task> {
    return this.http.put<Task>(
      `${this.apiUrl}/${id}`,
      task,
      this.getHeaders()
    );
  }

  deleteTask(id: number) {
    return this.http.delete(
      `${this.apiUrl}/${id}`,
      this.getHeaders()
    );
  }
}