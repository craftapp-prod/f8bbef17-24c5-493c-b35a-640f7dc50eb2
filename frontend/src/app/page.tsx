import Link from "next/link";
import { Shield, User, Lock } from "lucide-react";

export default function Home() {
  return (
    <div className="flex flex-col items-center">
      <section className="w-full py-12 md:py-24 text-center">
        <div className="container px-4 md:px-6">
          <div className="flex flex-col items-center space-y-4 text-center">
            <div className="space-y-2">
              <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl">
                Craftapp.ai
              </h1>
              <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl">
                Welcome to craftapp
              </p>
            </div>
            <div className="space-x-4">
              <Link
                href="#"
                className="inline-flex h-10 items-center justify-center rounded-md bg-primary-600 px-8 text-sm font-medium text-white shadow transition-colors hover:bg-primary-700 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-primary-500"
              >
                Get Started
              </Link>
            </div>
          </div>
        </div>
      </section>

      <section className="w-full py-12 md:py-24 bg-gray-100">
        <div className="container px-4 md:px-6">
          <div className="mx-auto flex max-w-[58rem] flex-col items-center space-y-4 text-center">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl">
              Key Features
            </h2>
            <p className="max-w-[85%] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
              Modern full-stack web application, single page application, real
              time game....
            </p>
          </div>
          <div className="mx-auto grid max-w-5xl grid-cols-1 gap-6 py-12 md:grid-cols-3">
            <div className="flex flex-col items-center space-y-2 rounded-lg border p-6 shadow-sm">
              <div className="p-3 rounded-full bg-primary-100">
                <User className="h-6 w-6 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold">Full-Stack web app</h3>
              <p className="text-sm text-gray-500 text-center">
                Complete user registration, authentication, and profile
                management...
              </p>
            </div>
            <div className="flex flex-col items-center space-y-2 rounded-lg border p-6 shadow-sm">
              <div className="p-3 rounded-full bg-primary-100">
                <Lock className="h-6 w-6 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold">Single Page app</h3>
              <p className="text-sm text-gray-500 text-center">
                amazing single page apps.
              </p>
            </div>
            <div className="flex flex-col items-center space-y-2 rounded-lg border p-6 shadow-sm">
              <div className="p-3 rounded-full bg-primary-100">
                <Shield className="h-6 w-6 text-primary-600" />
              </div>
              <h3 className="text-xl font-bold">Real time apps</h3>
              <p className="text-sm text-gray-500 text-center">
                Amazing real time app like game, stop watch ....
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="w-full py-12 md:py-24">
        <div className="container px-4 md:px-6">
          <div className="mx-auto max-w-[58rem] flex flex-col items-center justify-center space-y-4 text-center">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl">
              Ready to get started?
            </h2>
            <p className="max-w-[85%] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
              Create your own app now
            </p>
            <div className="flex flex-col gap-2 min-[400px]:flex-row">
              <Link
                href="#"
                className="inline-flex h-10 items-center justify-center rounded-md bg-primary-600 px-8 text-sm font-medium text-white shadow transition-colors hover:bg-primary-700 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-primary-500"
              >
                Start Now ...
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
